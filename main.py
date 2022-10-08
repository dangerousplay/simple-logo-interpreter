# This is a sample Python script.
import typing
from typing import List

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from antlr4 import *

from logoListener import logoListener
from logoLexer import logoLexer
from logoParser import logoParser

ANGLE = 0.0


class InvokeFunction:
    def __init__(self, function, declared_parameters=None):
        if declared_parameters is None:
            declared_parameters = {}

        self.function = function
        self.declared_parameters = declared_parameters

    def __call__(self, *args, **kwargs):
        parameters = self.declared_parameters.copy()

        for name, value in kwargs.items():
            for parameter_name, parameter_value in parameters.items():
                if parameter_value == name:
                    parameters[parameter_name] = value

        self.function(**parameters)


class Function:
    name: str
    parameters: List[str]
    body: List[InvokeFunction]

    def __init__(self, name, parameters, body):
        self.name = name
        self.parameters = parameters
        self.body = body

    def __call__(self, *args, **kwargs):
        arguments_size = len(args) + len(kwargs)

        if arguments_size != len(self.parameters):
            raise Exception(f"Expected {len(self.parameters)} parameters but {arguments_size} where informed")

        parameters = {}

        if len(args) > 0:
            for i, parameter in enumerate(self.parameters):
                parameters[parameter] = args[i]

        for name, value in kwargs.items():
            if name in self.parameters:
                parameters[name] = value
            else:
                raise Exception(f"Parameter {name} not exists for this function")

        for operation in self.body:
            operation(**parameters)

    @property
    def __name__(self):
        return self.name


def right(angle: float):
    global ANGLE
    ANGLE += angle


def left(angle: float):
    global ANGLE
    ANGLE -= angle


def penup():
    print("Turtle.set_draw(false)")


def pendown():
    print("Turtle.set_draw(true)")


def setxy(x, y):
    print(f"Turtle.set_position({x}, {y})")


def clear_screen():
    print(f"Turtle.clear()")
    print(f"Turtle.set_position(0, 0)")

    global ANGLE
    ANGLE = 0


def wipe_clean():
    print(f"Turtle.clear()")


def random():
    print("RANDOM")


def forward(num):
    print(f"Turtle.draw_segment({ANGLE}, {num})")


def backward(num):
    print(f"Turtle.draw_segment({ANGLE}, {num})")


def _parse_parameter_value_(parameter: logoParser.Function_argContext):
    parameter_value = parameter.SCIENTIFIC_NUMBER()

    if parameter_value is not None:
        parameter_value = float(parameter_value.getText())
    else:
        parameter_value = parameter.IDENTIFIER().getText()

    return parameter_value


def _invoke_builtin_(command: logoParser.CommandContext):
    commands = {
        command.forward(): (forward, ['num']),
        command.backward(): (backward, ['num']),
        command.right(): (right, ['angle']),
        command.left(): (left, ['angle']),
        command.setxy(): (setxy, ['x', 'y']),
        command.pendown(): (pendown, []),
        command.penup(): (penup, []),
        command.random(): (random, []),
        command.wipe_clean(): (wipe_clean, []),
        command.clear_screen(): (clear_screen, []),
    }

    for context, mapping in commands.items():
        if context is None:
            continue

        function, parameters = mapping

        function_parameters = _map_function_parameters_(context, parameters)

        return InvokeFunction(function, function_parameters)


def _map_function_parameters_(function, mapped_parameters: List[str]):
    function_parameters = {}

    function_declared_params = function.function_arg()
    function_declared_params = function_declared_params \
        if isinstance(function_declared_params, list) \
        else [function_declared_params]

    for func_mapped_param, declared_param in zip(mapped_parameters, function_declared_params):
        function_parameters[func_mapped_param] = _parse_parameter_value_(declared_param)

    return function_parameters


class LogoProgram(logoListener):
    symbol_table = {}

    def __init__(self):
        pass

    def exitFunction_body(self, ctx:logoParser.Function_bodyContext):
        print()
        pass

    def exitFunction_declaration(self, ctx:logoParser.Function_declarationContext):
        function_arguments = ctx.function_args_declaration().function_arg()
        function_arguments = list(map(lambda x: x.IDENTIFIER().getText(), function_arguments))

        function_declared_name = ctx.IDENTIFIER().getText()

        symbol = self.symbol_table.get(function_declared_name)

        if symbol is not None:
            raise Exception(f"A symbol already exists {symbol}")

        # commands: List[logoParser.Command_declare_invokeContext] = ctx.function_body().command_declare_invoke()
        # commands: List[logoParser.CommandContext] = list(map(lambda x: x.command(), commands))
        #

        statements: List[logoParser.Function_body_statementContext] = ctx.function_body().function_body_statement()

        body: List[InvokeFunction] = []

        for statement in statements:
            command = statement.command_declare_invoke()

            if command is not None:
                body.append(_invoke_builtin_(command.command()))
            else:
                function = statement.function_declare_invoke()

                function_to_invoke: Function = self.symbol_table.get(function.IDENTIFIER().getText())

                if function_to_invoke is None:
                    raise Exception(f"not found function to invoke: {function.IDENTIFIER()}")

                parameters = _map_function_parameters_(function, function_to_invoke.parameters)
                body.append(InvokeFunction(function_to_invoke, parameters))

        self.symbol_table[function_declared_name] = Function(function_declared_name, function_arguments, body)

    def exitInvoke_function(self, ctx:logoParser.Invoke_functionContext):
        function_name = ctx.IDENTIFIER().getText()

        function = self.symbol_table.get(function_name)

        if function is None:
            raise Exception(f"Function {function_name} not found")

        parameters = map(lambda x: float(x.getText()), ctx.SCIENTIFIC_NUMBER())
        parameters = list(parameters)

        function(*parameters)

    def exitInvoke_command(self, ctx:logoParser.Invoke_commandContext):
        _invoke_builtin_(ctx.command())()


def parse_file(path):
  lexer = logoLexer(FileStream(path))
  stream = CommonTokenStream(lexer)
  parser = logoParser(stream)
  program = LogoProgram()

  parser.addParseListener(program)
  parser.file_()


if __name__ == "__main__":
  parse_file('./examples/commands.lo')

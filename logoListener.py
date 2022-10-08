# Generated from logo.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .logoParser import logoParser
else:
    from logoParser import logoParser

# This class defines a complete listener for a parse tree produced by logoParser.
class logoListener(ParseTreeListener):

    # Enter a parse tree produced by logoParser#file_.
    def enterFile_(self, ctx:logoParser.File_Context):
        pass

    # Exit a parse tree produced by logoParser#file_.
    def exitFile_(self, ctx:logoParser.File_Context):
        pass


    # Enter a parse tree produced by logoParser#program.
    def enterProgram(self, ctx:logoParser.ProgramContext):
        pass

    # Exit a parse tree produced by logoParser#program.
    def exitProgram(self, ctx:logoParser.ProgramContext):
        pass


    # Enter a parse tree produced by logoParser#invoke_function.
    def enterInvoke_function(self, ctx:logoParser.Invoke_functionContext):
        pass

    # Exit a parse tree produced by logoParser#invoke_function.
    def exitInvoke_function(self, ctx:logoParser.Invoke_functionContext):
        pass


    # Enter a parse tree produced by logoParser#function_declaration.
    def enterFunction_declaration(self, ctx:logoParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by logoParser#function_declaration.
    def exitFunction_declaration(self, ctx:logoParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by logoParser#function_args_declaration.
    def enterFunction_args_declaration(self, ctx:logoParser.Function_args_declarationContext):
        pass

    # Exit a parse tree produced by logoParser#function_args_declaration.
    def exitFunction_args_declaration(self, ctx:logoParser.Function_args_declarationContext):
        pass


    # Enter a parse tree produced by logoParser#function_arg.
    def enterFunction_arg(self, ctx:logoParser.Function_argContext):
        pass

    # Exit a parse tree produced by logoParser#function_arg.
    def exitFunction_arg(self, ctx:logoParser.Function_argContext):
        pass


    # Enter a parse tree produced by logoParser#function_body.
    def enterFunction_body(self, ctx:logoParser.Function_bodyContext):
        pass

    # Exit a parse tree produced by logoParser#function_body.
    def exitFunction_body(self, ctx:logoParser.Function_bodyContext):
        pass


    # Enter a parse tree produced by logoParser#function_body_statement.
    def enterFunction_body_statement(self, ctx:logoParser.Function_body_statementContext):
        pass

    # Exit a parse tree produced by logoParser#function_body_statement.
    def exitFunction_body_statement(self, ctx:logoParser.Function_body_statementContext):
        pass


    # Enter a parse tree produced by logoParser#function_declare_invoke.
    def enterFunction_declare_invoke(self, ctx:logoParser.Function_declare_invokeContext):
        pass

    # Exit a parse tree produced by logoParser#function_declare_invoke.
    def exitFunction_declare_invoke(self, ctx:logoParser.Function_declare_invokeContext):
        pass


    # Enter a parse tree produced by logoParser#command_declare_invoke.
    def enterCommand_declare_invoke(self, ctx:logoParser.Command_declare_invokeContext):
        pass

    # Exit a parse tree produced by logoParser#command_declare_invoke.
    def exitCommand_declare_invoke(self, ctx:logoParser.Command_declare_invokeContext):
        pass


    # Enter a parse tree produced by logoParser#invoke_command.
    def enterInvoke_command(self, ctx:logoParser.Invoke_commandContext):
        pass

    # Exit a parse tree produced by logoParser#invoke_command.
    def exitInvoke_command(self, ctx:logoParser.Invoke_commandContext):
        pass


    # Enter a parse tree produced by logoParser#command.
    def enterCommand(self, ctx:logoParser.CommandContext):
        pass

    # Exit a parse tree produced by logoParser#command.
    def exitCommand(self, ctx:logoParser.CommandContext):
        pass


    # Enter a parse tree produced by logoParser#forward.
    def enterForward(self, ctx:logoParser.ForwardContext):
        pass

    # Exit a parse tree produced by logoParser#forward.
    def exitForward(self, ctx:logoParser.ForwardContext):
        pass


    # Enter a parse tree produced by logoParser#backward.
    def enterBackward(self, ctx:logoParser.BackwardContext):
        pass

    # Exit a parse tree produced by logoParser#backward.
    def exitBackward(self, ctx:logoParser.BackwardContext):
        pass


    # Enter a parse tree produced by logoParser#left.
    def enterLeft(self, ctx:logoParser.LeftContext):
        pass

    # Exit a parse tree produced by logoParser#left.
    def exitLeft(self, ctx:logoParser.LeftContext):
        pass


    # Enter a parse tree produced by logoParser#right.
    def enterRight(self, ctx:logoParser.RightContext):
        pass

    # Exit a parse tree produced by logoParser#right.
    def exitRight(self, ctx:logoParser.RightContext):
        pass


    # Enter a parse tree produced by logoParser#penup.
    def enterPenup(self, ctx:logoParser.PenupContext):
        pass

    # Exit a parse tree produced by logoParser#penup.
    def exitPenup(self, ctx:logoParser.PenupContext):
        pass


    # Enter a parse tree produced by logoParser#pendown.
    def enterPendown(self, ctx:logoParser.PendownContext):
        pass

    # Exit a parse tree produced by logoParser#pendown.
    def exitPendown(self, ctx:logoParser.PendownContext):
        pass


    # Enter a parse tree produced by logoParser#setxy.
    def enterSetxy(self, ctx:logoParser.SetxyContext):
        pass

    # Exit a parse tree produced by logoParser#setxy.
    def exitSetxy(self, ctx:logoParser.SetxyContext):
        pass


    # Enter a parse tree produced by logoParser#random.
    def enterRandom(self, ctx:logoParser.RandomContext):
        pass

    # Exit a parse tree produced by logoParser#random.
    def exitRandom(self, ctx:logoParser.RandomContext):
        pass


    # Enter a parse tree produced by logoParser#wipe_clean.
    def enterWipe_clean(self, ctx:logoParser.Wipe_cleanContext):
        pass

    # Exit a parse tree produced by logoParser#wipe_clean.
    def exitWipe_clean(self, ctx:logoParser.Wipe_cleanContext):
        pass


    # Enter a parse tree produced by logoParser#clear_screen.
    def enterClear_screen(self, ctx:logoParser.Clear_screenContext):
        pass

    # Exit a parse tree produced by logoParser#clear_screen.
    def exitClear_screen(self, ctx:logoParser.Clear_screenContext):
        pass



del logoParser
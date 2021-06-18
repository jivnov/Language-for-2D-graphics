from typing import List

from antlr4 import *

from TwoDimLexer import TwoDimLexer


class TwoDimParserBase ( Parser ):
    def __init__(self, _input: BufferedTokenStream, output):
        super().__init__(_input, output)

    """
     Returns {@code True} iff on the current index of the parser's
     token stream a token exists on the {@code HIDDEN} channel which
     either is a line terminator, or is a multi line comment that
     contains a line terminator.
    
     @return {@code True} iff on the current index of the parser's
     token stream a token exists on the {@code HIDDEN} channel which
     either is a line terminator, or is a multi line comment that
     contains a line terminator.
     """
    def lineTerminatorAhead(self) -> bool:
        # Get the token ahead of the current index.
        possibleIndexEosToken: int = self.getCurrentToken().tokenIndex - 1

        if possibleIndexEosToken == -1:
            return True

        ahead: Token = self._input.get(possibleIndexEosToken)
        if ahead.channel != Lexer.HIDDEN:
            # We're only interested in tokens on the HIDDEN channel.
            return False

        if ahead.type == TwoDimLexer.TERMINATOR:
            # There is definitely a line terminator ahead.
            return True

        if ahead.type == TwoDimLexer.WS:
            # Get the token ahead of the current whitespaces.
            possibleIndexEosToken = self.getCurrentToken().tokenIndex - 2
            ahead = self._input.get(possibleIndexEosToken)

        # Get the token's text and type.
        text: str = ahead.text
        typeN: int = ahead.type

        # Check if the token is, or contains a line terminator.
        return (typeN == TwoDimLexer.COMMENT and ("\r" in text or "\n" in text)) or (typeN == TwoDimLexer.TERMINATOR)

     
    #  Returns {@code True} if no line terminator exists between the specified
    #  token offset and the prior one on the {@code HIDDEN} channel.
     
    #  @return {@code True} if no line terminator exists between the specified
    #   token offset and the prior one on the {@code HIDDEN} channel.
     
    def noTerminatorBetween(self, tokenOffset: int) -> bool:
        stream: BufferedTokenStream = self._input
        tokens: List[Token] = stream.getHiddenTokensToLeft(stream.LT(tokenOffset).tokenIndex)
        
        if tokens == None:
            return True

        for token in tokens:
            if "\n" in token.text:
                return False

        return True

    
    # Returns {@code True} if no line terminator exists after any encounterd
    # parameters beyond the specified token offset and the next on the
    # {@code HIDDEN} channel.
    #
    # @return {@code True} if no line terminator exists after any encounterd
    # parameters beyond the specified token offset and the next on the
    # {@code HIDDEN} channel. 
    def noTerminatorAfterParams(self, tokenOffset: int) -> bool:
        stream: BufferedTokenStream = self._input
        leftParams = 1
        rightParams = 0

        if stream.LT(tokenOffset).type == TwoDimLexer.L_PAREN:
            # Scan past parameters
            while leftParams != rightParams:
                tokenOffset += 1
                valueType = stream.LT(tokenOffset).type

                if valueType == TwoDimLexer.L_PAREN:
                    leftParams += 1
                elif valueType == TwoDimLexer.R_PAREN:
                    rightParams += 1
            tokenOffset += 1
            return self.noTerminatorBetween(tokenOffset)

        return True

    def checkPreviousTokenText(self, text: str) -> bool:
        stream: BufferedTokenStream = self._input
        prevTokenText: str = stream.LT(1).text
        
        if prevTokenText == None:
            return False
        
        return prevTokenText == text
from antlr4 import *
from typing import List

class TwoDimParserBase ( Parser ):
    def __init__(self, input: TokenStream, output):
        super().__init__(input, output)

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
        possibleIndexEosToken: int = self.getCurrentToken().getTokenIndex() - 1

        if possibleIndexEosToken == -1:
            return True

        ahead: Token = _input.get(possibleIndexEosToken)
        if ahead.getChannel() != Lexer.HIDDEN:
            # We're only interested in tokens on the HIDDEN channel.
            return False

        if ahead.getType() == TwoDimLexer.TERMINATOR:
            # There is definitely a line terminator ahead.
            return True

        if ahead.getType() == TwoDimLexer.WS:
            # Get the token ahead of the current whitespaces.
            possibleIndexEosToken = self.getCurrentToken().getTokenIndex() - 2
            ahead = _input.get(possibleIndexEosToken)

        # Get the token's text and type.
        text: str = ahead.getText()
        typeN: int = ahead.getType()

        # Check if the token is, or contains a line terminator.
        return (typeN == TwoDimLexer.COMMENT and ("\r" in text or "\n" in text)) or (typeN == TwoDimLexer.TERMINATOR)

     
    #  Returns {@code True} if no line terminator exists between the specified
    #  token offset and the prior one on the {@code HIDDEN} channel.
     
    #  @return {@code True} if no line terminator exists between the specified
    #   token offset and the prior one on the {@code HIDDEN} channel.
     
    def noTerminatorBetween(self, tokenOffset: int) -> bool:
        stream: BufferedTokenStream = _input
        tokens: List[Token] = stream.getHiddenTokensToLeft(stream.LT(tokenOffset).getTokenIndex())
        
        if tokens == None:
            return True

        for token in tokens:
            if "\n" in token.getText():
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
        stream: BufferedTokenStream = _input
        leftParams = 1
        rightParams = 0
        valueType

        if stream.LT(tokenOffset).getType() == TwoDimLexer.L_PAREN:
            # Scan past parameters
            while leftParams != rightParams:
                tokenOffset += 1
                valueType = stream.LT(tokenOffset).getType()

                if valueType == TwoDimLexer.L_PAREN:
                    leftParams += 1
                elif valueType == TwoDimLexer.R_PAREN:
                    rightParams += 1
            tokenOffset += 1
            return noTerminatorBetween(tokenOffset)

        return True

    def checkPreviousTokenText(text: str) -> bool:
        stream: BufferedTokenStream = _input
        prevTokenText: str = stream.LT(1).getText()
        
        if prevTokenText == None:
            return False
        
        return prevTokenText.equals(text)
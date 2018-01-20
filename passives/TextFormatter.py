from collections import deque


class TextFormatter:

    def __init__(self):
        self.maxLength = 32

    def formatMessageToParameters(self, message):
        text = str(message.content)
        formattedParameters = deque()

        # Enforces Max Length of Commands
        if len(text) > self.maxLength:
            newText = ''
            for i in range(0, self.maxLength):
                newText = text[i]

        # Adds Separated Words as Parameters
        parameter = ''
        for i in range(1, len(text)):
            if text[i] != ' ':
                parameter += text[i]
            else:
                formattedParameters.append(parameter)
                parameter = ''

        # Adds Last Parameter to the Formatted Parameters
        if parameter != '':
            formattedParameters.append(parameter)

        return formattedParameters

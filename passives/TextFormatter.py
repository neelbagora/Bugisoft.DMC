from collections import deque


class TextFormatter:

    @staticmethod
    def formatMessageToParameters():
        from Leak import message
        text = str(message.content)
        formattedParameters = deque()

        # Enforces Max Length of Commands
        if len(text) > 32:
            newText = ''
            for i in range(0, 32):
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

class TranslationDirectoryNotFoundException(Exception):
    """Exception raised for translation directory not found."""

    def __init__(self, directory_name: str):
        self.directory_name = directory_name
        self.message = f"Translation directory '{directory_name}' not found."
        super().__init__(self.message)
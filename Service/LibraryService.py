from libraryUsingFiles.Service.BookService import BookService
from libraryUsingFiles.Service.UserService import UserService


class LibraryService: 
    def __init__(self) -> None:
        self.userService = UserService()
        self.bookService= BookService()

    
class ZeroProductQuantity(Exception):
    """Класс исключений товаров с нулевым количеством"""
    def _init__(self, message=None):
        super().__init__(message)

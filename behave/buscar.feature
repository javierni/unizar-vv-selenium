Feature: Buscar en la web del Ayuntamiento de Zaragoza

Scenario: Un usuario busca la palabra turismo en la web del Ayuntamiento de Zaragoza
  Given El usuario está en la página inicial de la web del Ayuntamiento de Zaragoza
  When Hace clic en el botón de búsqueda
  When Introduce como palabra de búsqueda "turismo"
  Then Aparece la página de resultados



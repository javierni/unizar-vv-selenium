from behave import *
from functions import MyFunctions

@given(u'El usuario está en la página inicial de la web del Ayuntamiento de Zaragoza')
def step_impl(context):
    MyFunctions.enterMainPage(context)

@when(u'Hace clic en el botón de búsqueda')
def step_impl(context):
    MyFunctions.clickSearchButton(context)

@when(u'Introduce como palabra de búsqueda "{keyword}"')
def step_impl(context, keyword):
    MyFunctions.enterKeyword(context, keyword)

@then(u'Aparece la página de resultados')
def step_impl(context):
    MyFunctions.resultsPageIsOpen(context)
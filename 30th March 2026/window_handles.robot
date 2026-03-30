*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/windows

*** Test Cases ***
Handling Windows
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Click Element    xpath=//a[@href='/windows/new']
    @{windows}  Get Window Handles
    @{titles}   Get Window Titles


    Switch Window  NEW
    Page Should Contain Element    xpath=//h3[text()="New Window"]
    Switch Window   ${windows}[0]
    Sleep    2s
    Close Browser



*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Windows
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Scroll Element Into View    xpath=//button[@id='PopUp']
    Sleep    2s
    Click Element    xpath=//button[@id='PopUp']
    Sleep    2s
    @{windows}  Get Window Handles
    @{titles}   Get Window Titles
    Log To Console    ${titles}[1]
    Switch Window  NEW
    Sleep    4s
    Switch Window   ${titles}[0]
    Log To Console    ${titles}[0]

    Close Browser
*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${url}  https://testautomationpractice.blogspot.com/
*** Test Cases ***
Simple Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Scroll Element Into View    //button[@onclick='myFunction()']
    Sleep    2s
    Click Button    xpath=//button[@id='alertBtn']
    Handle Alert
    Sleep    2s
    Close Browser
Confirmation Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Click Button    xpath=//button[@id="confirmBtn"]
    Sleep    2s
    Handle Alert  action=DISMISS
    Page Should Contain  You pressed Cancel!
    ${txt}  Get Text  xpath=//p[@id='demo']
    Log To Console    ${txt}
    Sleep    2s
    Close Browser

Prompt Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Click Button    xpath=//button[@id="promptBtn"]
    Sleep    2s
    Input Text Into Alert    Aayush
    Sleep    2s
    ${txt}  Get Text  xpath=//p[@id='demo']
    Log To Console    ${txt}
    Sleep    2s
    Close Browser
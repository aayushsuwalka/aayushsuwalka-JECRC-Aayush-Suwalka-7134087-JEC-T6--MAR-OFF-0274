*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
*** Variables ***
${url}  https://the-internet.herokuapp.com/
${check_downloaded}  C:\\Users\\aayus_ucf5jw3\\Downloads\\abc.txt
*** Test Cases ***
Upload
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Click Element    xpath=//a[@href='/upload']
    Sleep    2s
    ${path}  Normalize Path  ${CURDIR}/temp.txt
    Choose File    id=file-upload    ${path}
    Sleep    2s
    Click Button    id=file-submit
Download
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Click Element    xpath=//a[@href="/download"]
    Sleep    2s
    Click Element    xpath=//a[@href="download/abc.txt"]
    Sleep    2s
    Wait Until Created    ${check_downloaded}  timeout=10s
    File Should Exist    ${check_downloaded}
    Log To Console    It downloaded successfully

    Close Browser
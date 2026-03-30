*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://www.amazon.in/
*** Test Cases ***
Navigate
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Click Element    xpath=(//div[@id="nav-xshop-container"]/descendant::li[@class='nav-li'])[11]
    Sleep    2s
    Click Element    xpath=(//span[@class='a-size-base a-color-base'])[6]
    Sleep    2s
    ${item}  Get Text    (//div[@data-cy='title-recipe'])[6]
    Log To Console    ${item}
    Click Element    (//div[@data-cy='title-recipe'])[6]
    Sleep    2s
    Switch Window  NEW
    Page Should Contain    ${item}
    Sleep    2s
    ${d_price}  Get Text    xpath=(//div[@class='a-section a-spacing-none aok-align-center aok-relative apex-core-price-identifier'])[1]
    Log To Console    ${d_price}
    ${a_price}  Get Text    xpath=//div[@class='a-section a-spacing-small aok-align-center']
    Log To Console    ${a_price}
    Sleep    2s
    Scroll Element Into View    xpath=(//span[text()="Add to cart"])[3]
    Click Element    xpath=(//span[text()="Add to cart"])[3]/preceding-sibling::input
    Sleep    2s
    Click Element    xpath=//div[@class='layoutToolbarPadding']/descendant::div[@id='nav-cart-count-container']
    Sleep  2s
    Page Should Contain    ${item}
    Sleep    2s
    Close Browser


    
    Close Browser
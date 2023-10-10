*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      https://hrm.allweb.com.kh/login
${BROWSER}        Chrome

*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Maximize Browser Window
    Wait 1sec
    Input Username    porhong.keat@allweb.com.kh
    Wait 1sec
    Input Password    cAmbodi@168c
    Wait 1sec
    Login
    Wait 1sec
    Welcome Page Should Be Open
    Wait 1sec
    clock in
    Wait 5sec

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Human Resource Management System - Login
Input Username
    [Arguments]    ${email}
    Input Text    email   ${email}
Input Password
    [Arguments]    ${password}
    Input Text    password    ${password}
Login
    Click Button    //button[@type='submit']

Welcome Page Should Be Open
    Title Should Be    Dashboard

clock in
    Click Button   (//button[@id='clock_in'])[1]   
Wait 1sec
    Sleep  1s
Wait 5sec
    Sleep  5s
const {Builder, By, Key, ulit} = require ("selenium-webdriver");
const firefox = require("selenium-webdriver/firefox");
const fs = require("fs");
const { throws } = require("assert");
const { AssertionError } = require("assert/strict");

async function test(){
    let options = new firefox.Options();
    options.addArguments("-headless");
    let driver = await new Builder().forBrowser("firefox").setFirefoxOptions(options).build();
    await driver.get("http://localhost:8008");
    await driver.findElement(By.id("postCard-1")).click();
    driver.findElement(By.id('updatepost')).then(function(webElement) {
        print('Update exists');
    }, function(err) {
        if (err.state && err.state === 'no such element') {
            print('Element not found');
        }
    });
    driver.findElement(By.id('deletepost')).then(function(webElement) {
        print('Delete exists');
    }, function(err) {
        if (err.state && err.state === 'no such element') {
            print('Element not found');
        }
    });
    driver.findElement(By.id('commentauthor')).then(function(webElement) {
        print('Comment author exists');
        webElement.sendKeys("Tester Author");
    }, function(err) {
        if (err.state && err.state === 'no such element') {
            print('Element not found');
         }
    });
    //await driver.findElement(By.id("commentauthor")).sendKeys("Tester Author");
    driver.findElement(By.id('commentarea')).then(function(webElement) {
        print('Comment area exists');
        webElement.sendKeys("Testing comment area");
    }, function(err) {
        if (err.state && err.state === 'no such element') {
            print('Element not found');
        }
    });
    driver.findElement(By.id('commentsubmit')).then(function(webElement) {
        print('Comment submit button exists');
        webElement.click();
    }, function(err) {
        if (err.state && err.state === 'no such element') {
            print('Element not found');
        }
    });
    await driver.quit();
}

test();
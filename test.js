const {Builder, By, Key, ulit} = require ("selenium-webdriver");
const firefox = require("selenium-webdriver/firefox");
const fs = require("fs");

async function test(){
    let options = new firefox.Options();
    options.addArguments("-headless");
    let driver = await new Builder().forBrowser("firefox").setFirefoxOptions(options).build();
    await driver.get("http://localhost:8008");
    await driver.findElement(By.id("postCard-1")).click();
    driver.findElement(By.id('updatepost')).then(function(webElement) {
        console.log('Update exists');
    }, function(err) {
        if (err.state && err.state === 'no such element') {
            console.log('Element not found');
        } else {
            driver.promise.rejected(err);
        }
    });
    driver.findElement(By.id('deletepost')).then(function(webElement) {
        console.log('Delete exists');
    }, function(err) {
        if (err.state && err.state === 'no such element') {
            console.log('Element not found');
        } else {
            driver.promise.rejected(err);
        }
    });
    driver.findElement(By.id('commentauthor')).then(function(webElement) {
        console.log('Comment author exists');
        webElement.sendKeys("Tester Author");
    }, function(err) {
        if (err.state && err.state === 'no such element') {
            console.log('Element not found');
        } else {
            driver.promise.rejected(err);
        }
    });
    //await driver.findElement(By.id("commentauthor")).sendKeys("Tester Author");
    driver.findElement(By.id('commentarea')).then(function(webElement) {
        console.log('Comment area exists');
        webElement.sendKeys("Testing comment area");
    }, function(err) {
        if (err.state && err.state === 'no such element') {
            console.log('Element not found');
        } else {
            driver.promise.rejected(err);
        }
    });
    driver.findElement(By.id('commentsubmit')).then(function(webElement) {
        console.log('Comment submit button exists');
        webElement.click();
    }, function(err) {
        if (err.state && err.state === 'no such element') {
            console.log('Element not found');
        } else {
            driver.promise.rejected(err);
        }
    });
    await driver.quit();
}

test();
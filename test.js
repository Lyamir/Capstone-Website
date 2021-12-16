const {Builder, By, Key, ulit, WebDriver} = require ("selenium-webdriver");
const firefox = require("selenium-webdriver/firefox");
const { assert } = require("assert");

async function test(){
    let options = new firefox.Options();
    options.addArguments("-headless");
    let driver = await new Builder().forBrowser("firefox").setFirefoxOptions(options).build();
    await driver.get("http://localhost:8008");
    await driver.findElement(By.id("postCard-1")).click();

    await driver.findElement(By.id('commentauthor')).sendKeys("Tester author");
    await driver.findElement(By.id("commentarea")).sendKeys("Testing comment area");
    await driver.findElement(By.id('commentsubmit')).click();

    let testText = await driver.findElement(By.id("comment-1")).getText().then(function(value){
        return value;
    });

    console.log(testText);

    assert.strictEqual(testText, "");

    // await driver.findElement(By.id('updateposts')).then(function() {
    //     console.log("Update exists");
    // }, function(err) {
    //     if (err) {
    //         console.log('Update not found');
    //     } else {
    //         webElement.promise.rejected(err);
    //     }
    // });
    // await driver.findElement(By.id('deletepost')).then(function(webElement) {
    //     console.log('Delete exists');
    // }, function(err) {
    //     if (err) {
    //         console.log('Delete not found');
    //     }  else {
    //         webElement.promise.rejected(err);
    //     }
    // });
    // await driver.findElement(By.id('commentauthor')).then(function(webElement) {
    //     console.log('Comment author exists');
    //     webElement.sendKeys("Tester Author");
    // }, function(err) {
    //     if (err.state && err.state === 'no such element') {
    //         console.log('Element not found');
    //      }
    // });
    // //await driver.findElement(By.id("commentauthor")).sendKeys("Tester Author");
    // await driver.findElement(By.id('commentarea')).then(function(webElement) {
    //     console.log('Comment area exists');
    //     webElement.sendKeys("Testing comment area");
    // }, function(err) {
    //     if (err.state && err.state === 'no such element') {
    //         console.log('Element not found');
    //     }
    // });
    // await driver.findElement(By.id('commentsubmit')).then(function(webElement) {
    //     console.log('Comment submit button exists');
    //     webElement.click();
    // }, function(err) {
    //     if (err.state && err.state === 'no such element') {
    //         console.log('Element not found');
    //     }
    // });
    await driver.quit();
}

test();
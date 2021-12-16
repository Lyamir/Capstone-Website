const {Builder, By, Key, ulit, WebDriver} = require ("selenium-webdriver");
const firefox = require("selenium-webdriver/firefox");
const  assert = require("assert");

async function test(){
    let options = new firefox.Options();
    options.addArguments("-headless");
    let driver = await new Builder().forBrowser("firefox").setFirefoxOptions(options).build();
    await driver.get("http://localhost:8008");
    await driver.findElement(By.id("postCard-1")).click();

    let titleText = await driver.findElement(By.className("title")).getText().then(function(value){
        return value;
    });
    
    assert.strictEqual(titleText, "Goodbye World");

    await driver.findElement(By.id('commentauthor')).sendKeys("Tester author");
    await driver.findElement(By.id("commentarea")).sendKeys("Testing comment area");
    await driver.findElement(By.id('commentsubmit')).click();

    await driver.quit();
}

test();
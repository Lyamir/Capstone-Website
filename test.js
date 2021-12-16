const {Builder, By, Key, ulit} = require ("selenium-webdriver");
const firefox = require("selenium-webdriver/firefox");
const fs = require("fs");

async function test(){
    let options = new firefox.Options();
    options.addArguments("-headless");
    let driver = await new Builder().forBrowser("firefox").setFirefoxOptions(options).build();
    await driver.get("http://localhost:8008");
    await driver.findElement(By.id("postCard-1")).click();
    await driver.findElement(By.id("updatepost")).click();
    await driver.back();
    await driver.findElement(By.id("deletepost")).click();  
    await driver.back();
    await driver.findElement(By.id("commentauthor")).sendKeys("Tester Author");
    await driver.findElement(By.id("commentarea")).sendKeys("Testing comment area");
    await driver.findElement(By.id("commentsubmit")).click();
    await driver.quit();
}

test();
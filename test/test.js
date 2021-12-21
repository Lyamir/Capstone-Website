const {Builder, By, Key, ulit, WebDriver} = require ("selenium-webdriver");
const firefox = require("selenium-webdriver/firefox");
const  assert = require("assert");
const chai = require("chai");
const chaihttp = require("chai-http");
const app = require("../index");

chai.should();
chai.use(chaihttp);

describe("Unit Tests", function(){
    it("It should GET all posts", function(){
        chai.request(app)
            .get("index")
            .end((function(err, response){
                response.should.have.status(200);
                done();
            }));
    });
});






async function test(){
    let options = new firefox.Options();
    options.addArguments("-headless");
    let driver = await new Builder().forBrowser("firefox").setFirefoxOptions(options).build();
    await driver.get("http://localhost:8008");
    await driver.findElement(By.id("postCard-1")).click();

    let titleText = await driver.findElement(By.className("title")).getText().then(function(value){
        return value;
    });

    assert.strictEqual(titleText, "Goodbye WorldAAA");

    await driver.findElement(By.id('commentauthor')).sendKeys("Tester author");
    await driver.findElement(By.id("commentarea")).sendKeys("Testing comment area");
    await driver.findElement(By.id('commentsubmit')).click();

    await driver.quit();
}
test();
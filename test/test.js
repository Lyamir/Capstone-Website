const {Builder, By, Key, ulit, WebDriver} = require ("selenium-webdriver");
const firefox = require("selenium-webdriver/firefox");
const  assert = require("assert");
const should = require("chai").should();

describe("Unit Tests", function(){

    it("It should GET all posts", async function(){
        console.log("all posts is retrieved, some are updated or deleted");
        let options = new firefox.Options();
        options.addArguments("-headless");
        let driver = await new Builder().forBrowser("firefox").setFirefoxOptions(options).build();
        await driver.get("http://localhost:8008");

        let resultPost1 = await driver.findElement(By.xpath("/html/body/div/a[1]/div")).getText();
        let resultPost2 = await driver.findElement(By.xpath("/html/body/div/a[2]/div")).getText();
        let resultPost3 = await driver.findElement(By.xpath("/html/body/div/a[3]/div")).getText();
        let post1 = "1\nGoodbye World\nWed Oct 27 2021 00:00:00 GMT+0000 (Coordinated Universal Time)\nadmin"
        let post2 = "2\nTest Post\nWed Oct 27 2021 22:26:02 GMT+0000 (Coordinated Universal Time)\njohn"
        let post3 = "3\nTest Post 2\nWed Oct 27 2021 22:28:45 GMT+0000 (Coordinated Universal Time)\nadmin"

        resultPost1.should.equal(post1);
        resultPost2.should.equal(post2);
        resultPost3.should.equal(post3);

        await driver.quit();
    });
});

describe("Integration Tests", async function(){
    it("It should display a page", async function(){
        console.log("a page is displayed with the expected output");
        let options = new firefox.Options();
        options.addArguments("-headless");
        let driver = await new Builder().forBrowser("firefox").setFirefoxOptions(options).build();
        await driver.get("http://localhost:8008");

        await driver.findElement(By.xpath("/html/body/div/a[1]/div"));
        await driver.findElement(By.xpath("/html/body/div/a[2]/div"));
        await driver.findElement(By.xpath("/html/body/div/a[3]/div")).click();
        
        let titleResult = await driver.findElement(By.xpath("/html/body/div/div/div[1]")).getText();
        let authorResult = await driver.findElement(By.xpath("/html/body/div/div/div[2]")).getText();
        let dateResult = await driver.findElement(By.xpath("/html/body/div/div/div[3]")).getText();
        let contentResult = await driver.findElement(By.xpath("/html/body/div/div/div[4]")).getText();

        let title = "Test Post 2";
        let author = "Created by: admin";
        let date = "Created on: Wed Oct 27 2021 22:28:45 GMT+0000 (Coordinated Universal Time)";
        let content = "This is another test post";

        titleResult.should.equal(title);
        authorResult.should.equal(author);
        dateResult.should.equal(date);
        contentResult.should.equal(content);

        await driver.findElement(By.xpath("//*[@id=\"updatepost\"]")).click();
        await driver.findElement(By.xpath("/html/body/div/div/form/div/button")).click();

        await driver.quit();
    });
});




// async function test(){
//     let options = new firefox.Options();
//     options.addArguments("-headless");
//     let driver = await new Builder().forBrowser("firefox").setFirefoxOptions(options).build();
//     await driver.get("http://localhost:8008");
//     await driver.findElement(By.id("postCard-1")).click();

//     let titleText = await driver.findElement(By.className("title")).getText().then(function(value){
//         return value;
//     });

//     assert.strictEqual(titleText, "Goodbye WorldAAA");

//     await driver.findElement(By.id('commentauthor')).sendKeys("Tester author");
//     await driver.findElement(By.id("commentarea")).sendKeys("Testing comment area");
//     await driver.findElement(By.id('commentsubmit')).click();

//     await driver.quit();
// }
// test();
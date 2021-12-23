const {Builder, By, Key, ulit, WebDriver, WebElement} = require ("selenium-webdriver");
const firefox = require("selenium-webdriver/firefox");
const  assert = require("assert");
const should = require("chai").should();
const expect = require("chai").expect();

describe("Unit Tests", async function(){

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

// describe("Integration Tests", async function(){

//     let post = {
//         title:"Integration Testing",
//         content:"Testing the integration of all modules",
//         author:"Tester"
//     }

//     let testingUpdate = "Integration Testing Update";

//     let testComment = {
//         author: "CommentTester",
//         comment: "Comment testing"
//     }

//     it("It should display a page", async function(){
//         console.log("a page is displayed with the expected output");
//         let options = new firefox.Options();
//         options.addArguments("-headless");
//         let driver = await new Builder().forBrowser("firefox").setFirefoxOptions(options).build();
//         await driver.get("http://localhost:8008");

//         await driver.findElement(By.xpath("/html/body/div/a[1]/div"));
//         await driver.findElement(By.xpath("/html/body/div/a[2]/div"));
//         await driver.findElement(By.xpath("/html/body/div/a[3]/div")).click();
        
//         let titleResult = await driver.findElement(By.xpath("/html/body/div/div/div[1]")).getText();
//         let authorResult = await driver.findElement(By.xpath("/html/body/div/div/div[2]")).getText();
//         let dateResult = await driver.findElement(By.xpath("/html/body/div/div/div[3]")).getText();
//         let contentResult = await driver.findElement(By.xpath("/html/body/div/div/div[4]")).getText();

//         let title = "Test Post 2";
//         let author = "Created by: admin";
//         let date = "Created on: Wed Oct 27 2021 22:28:45 GMT+0000 (Coordinated Universal Time)";
//         let content = "This is another test post";

//         titleResult.should.equal(title);
//         authorResult.should.equal(author);
//         dateResult.should.equal(date);
//         contentResult.should.equal(content);

//         await driver.findElement(By.xpath("//*[@id=\"updatepost\"]")).click();
//         await driver.findElement(By.xpath("/html/body/div/div/form/div/button")).click();

//         await driver.quit();
//     });

//     it("Testing post should not appear in the homepage", async function(){
//         let options = new firefox.Options();
//         options.addArguments("-headless");
//         let driver = await new Builder().forBrowser("firefox").setFirefoxOptions(options).build();
//         await driver.get("http://localhost:8008");

//         let testingPost = await driver.findElements(By.xpath("//*[contains(text(), \""+post.title+"\")]"));

//         testingPost.should.be.empty;

//         await driver.quit();
//     });

//     it("It should create a post", async function(){
//         let options = new firefox.Options();
//         options.addArguments("-headless");
//         let driver = await new Builder().forBrowser("firefox").setFirefoxOptions(options).build();
//         await driver.get("http://localhost:8008");

//         await driver.findElement(By.xpath("/html/body/header/a")).click();

//         await driver.findElement(By.xpath("/html/body/div/div/form/div/input[1]")).sendKeys(post.title);
//         await driver.findElement(By.xpath("/html/body/div/div/form/div/input[2]")).sendKeys(post.author);
//         await driver.findElement(By.xpath("/html/body/div/div/form/div/textarea")).sendKeys(post.content);
//         await driver.findElement(By.xpath("/html/body/div/div/form/div/button")).click();

//         //Test if the post exists in the homepage
//         await driver.navigate().to("http://localhost:8008");
//         let resultingElement = await driver.findElements(By.xpath("//*[contains(text(), \""+post.title+"\")]"));
//         resultingElement.should.not.be.empty;

//         await driver.quit();
//     });

//     it("It should update the created post", async function(){
//         let options = new firefox.Options();
//         options.addArguments("-headless");
//         let driver = await new Builder().forBrowser("firefox").setFirefoxOptions(options).build();
//         await driver.get("http://localhost:8008");

//         await driver.findElement(By.xpath("//*[contains(text(), \""+post.title+"\")]")).click();

//         await driver.findElement(By.xpath("//*[@id=\"updatepost\"]")).click();

//         await driver.findElement(By.xpath("/html/body/div/div/form/div/input[1]")).clear();
//         await driver.findElement(By.xpath("/html/body/div/div/form/div/input[1]")).sendKeys(testingUpdate);
//         await driver.findElement(By.xpath("/html/body/div/div/form/div/button")).click();

//         //Test if updates are reflected
//         let resultingTitle = await driver.findElement(By.xpath("/html/body/div/div/div[1]")).getText();
//         resultingTitle.should.equal(testingUpdate);

//         await driver.quit();
//     });

//     it("It should add a comment to the added post", async function(){
//         let options = new firefox.Options();
//         options.addArguments("-headless");
//         let driver = await new Builder().forBrowser("firefox").setFirefoxOptions(options).build();
//         await driver.get("http://localhost:8008");

//         await driver.findElement(By.xpath("//*[contains(text(), \""+testingUpdate+"\")]")).click();

//         await driver.findElement(By.xpath("//*[@id=\"commentauthor\"]")).sendKeys(testComment.author);
//         await driver.findElement(By.xpath("//*[@id=\"commentarea\"]")).sendKeys(testComment.comment);
//         await driver.findElement(By.xpath("//*[@id=\"commentsubmit\"]")).click();

//         //Test if comment has been added
//         let commentContent = await driver.findElements(By.xpath("//*[contains(text(), \""+testComment.comment+"\")]"));
//         let commentAuthor = await driver.findElements(By.xpath("//*[contains(text(), \""+testComment.author+"\")]"));
//         commentContent.push().should.equal(testComment.comment);
//         commentAuthor.push().should.equal(testComment.author);
        
//         await driver.quit();
//     });

//     it("It should delete the testing post", async function(){
//         let options = new firefox.Options();
//         options.addArguments("-headless");
//         let driver = await new Builder().forBrowser("firefox").setFirefoxOptions(options).build();
//         await driver.get("http://localhost:8008");

//         await driver.findElement(By.xpath("//*[contains(text(), \""+testingUpdate+"\")]")).click();

//         await driver.findElement(By.xpath("//*[@id=\"deletepost\"]")).click();

//         //Test if post has been deleted in homepage
//         await driver.navigate().to("http://localhost:8008");
//         let resultingElement = await driver.findElements(By.xpath("//*[contains(text(), \""+testingUpdate+"\")]"));
//         resultingElement.should.be.empty;
//         let oldResultingElement = await driver.findElements(By.xpath("//*[contains(text(), \""+post.title+"\")]"));
//         oldResultingElement.should.be.empty;

//         await driver.quit();
//     });
// });
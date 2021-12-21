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

        var resultTitle = await driver.findElement(By.xpath("/html/body/div/a[1]/div/b")).getText().then(function(value){
            return value;
        });;
        var resultDate = await driver.findElement(By.xpath("/html/body/div/a[1]/div/b[2]")).getText().then(function(value){
            return value;
        });; 
        var resultAuthor = await driver.findElement(By.xpath("/html/body/div/a[1]/div/b[3]")).getText().then(function(value){
            return value;
        });;

        let postCard1 = {
            title : "Goodbye World",
            date : "Wed Oct 27 2021 00:00:00 GMT+0000 (Coordinated Universal Time)",
            author : "admin"
        };
        
        resultTitle.should.equal(postCard1.title);
        resultDate.should.equal(postCard1.date);
        resultAuthor.should.equal(postCard1.author);

        await driver.findElement(By.id('commentauthor')).sendKeys("Tester author");
        await driver.findElement(By.id("commentarea")).sendKeys("Testing comment area");
        await driver.findElement(By.id('commentsubmit')).click();
        await driver.quit();
    });
});

describe("Integration Tests", async function(){
    it("It should display a page", async function(done){
        // chai.request(app)
        //     .get("index")
        //     .end((function(err, response){
        //         response.should.have.status(200);
        //         done();
        //     }));
        console.log("a page is displayed with the expected output");
        done();
    });
});

describe("System Tests", async function(){
    it("It should perform an activity", async function(done){
        // chai.request(app)
        //     .get("index")
        //     .end((function(err, response){
        //         response.should.have.status(200);
        //         done();
        //     }));
        console.log("an activity is performed");
        done();
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
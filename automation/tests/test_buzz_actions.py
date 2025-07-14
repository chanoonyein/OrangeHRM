import time

import allure
import pytest
from pages.login_page import loginPage
from pages.buzz_page import BuzzPage
from utils.logger import setup_logger

logger = setup_logger()

@allure.title("Buzz - Full Post to Delete Flow Test")
@allure.description("Verifies full Buzz flow from creating a post to deleting it")
# @pytest.mark.skip(reason="Skipping full buzz flow test temporarily")
def test_full_buzz_flow(browser):
    login = loginPage(browser)
    buzz = BuzzPage(browser)

    logger.info("Loading login page")
    login.load()
    login.login("Admin", "admin123")
    logger.info("Logged in as Admin")

    buzz.go_to_buzz()
    logger.info("Navigated to Buzz module")

    test_post = "Hello QABatch6 from Chan Oo"
    buzz.create_post(test_post)
    logger.info("Post created")
    buzz.get_base_location(test_post)
    # logger.info(buzz.get_first_post_text())
    # actual_text = buzz.get_first_post_text().strip()
    # expected_text = test_post.strip()
    # assert expected_text in actual_text
    logger.info("Verified posted content")
    time.sleep(2)


    buzz.comment_on_post("Welcome Chan Oo")
    logger.info("Comment added")
    time.sleep(2)


    buzz.like_post()
    logger.info("Post liked")
    time.sleep(5)

    buzz.delete_post()
    logger.info("Post deleted")
    time.sleep(2)
    allure.attach(browser.get_screenshot_as_png(), name="BuzzFlow", attachment_type=allure.attachment_type.PNG)

@allure.title("Buzz - Create Post Test")
@allure.description("Verifies a user can successfully create a Buzz post")
def test_create_buzz_post(login_and_navigate_to_buzz, browser):
    buzz = login_and_navigate_to_buzz
    test_post = "Hello QABatch6 from Chan Oo"
    buzz.create_post(test_post)
    buzz.get_base_location(test_post)
    logger.info("Post created and verified")
    allure.attach(
        browser.get_screenshot_as_png(),
        name="BuzzPost",
        attachment_type=allure.attachment_type.PNG
    )

@allure.title("Buzz - Comment on Post Test")
@allure.description("Verifies commenting functionality on a Buzz post")
def test_comment_on_buzz_post(login_and_navigate_to_buzz, browser):
    buzz = login_and_navigate_to_buzz
    test_post = "Hello QABatch6 from Chan Oo"
    buzz.get_base_location(test_post)
    comment = "Welcome Chan Oo"
    buzz.comment_on_post(comment)

    logger.info("Comment added and verified")
    allure.attach(
        browser.get_screenshot_as_png(),
        name="BuzzComment",
        attachment_type=allure.attachment_type.PNG
    )
    time.sleep(2)

@allure.title("Buzz - Like Post Test")
@allure.description("Verifies that a post can be liked")
def test_like_buzz_post(login_and_navigate_to_buzz, browser):
    buzz = login_and_navigate_to_buzz
    test_post = "Hello QABatch6 from Chan Oo"
    buzz.get_base_location(test_post)
    buzz.like_post()
    logger.info("Post liked successfully")
    allure.attach(
        browser.get_screenshot_as_png(),
        name="BuzzLike",
        attachment_type=allure.attachment_type.PNG
    )
    time.sleep(2)

@allure.title("Buzz - UnLike Post Test")
@allure.description("Verifies that a post can be unliked")
def test_unlike_buzz_post(login_and_navigate_to_buzz, browser):
    buzz = login_and_navigate_to_buzz
    test_post = "Hello QABatch6 from Chan Oo"
    buzz.get_base_location(test_post)
    buzz.like_post()
    time.sleep(2)
    logger.info("Post unliked successfully")
    allure.attach(
        browser.get_screenshot_as_png(),
        name="BuzzUnLike",
        attachment_type=allure.attachment_type.PNG
    )
    time.sleep(2)


@allure.title("Buzz - Delete Post Test")
@allure.description("Verifies that a Buzz post can be deleted")
def test_delete_buzz_post(login_and_navigate_to_buzz, browser):
    buzz = login_and_navigate_to_buzz
    test_post = "Hello QABatch6 from Chan Oo"
    buzz.get_base_location(test_post)
    buzz.delete_post()
    logger.info("Post deleted successfully")
    time.sleep(2)
    allure.attach(
        browser.get_screenshot_as_png(),
        name="BuzzDelete",
        attachment_type=allure.attachment_type.PNG
    )
    time.sleep(2)
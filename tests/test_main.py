import json
from fastapi.testclient import TestClient
from main import app, fake, Post, Comment, Profile
import logging
import sys
import os
import pytest
from allure_commons.types import AttachmentType
from allure_commons._allure import attach

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

def test_generate_post():
    post = Post(
        id=fake.random_int(),
        title=fake.sentence(),
        author=fake.name()
    )
    logging.info(f"Generated post: {post}")
    attach(post.title, name="Post Title", attachment_type=AttachmentType.TEXT)
    assert isinstance(post.id, int)
    assert post.title != ""
    assert post.author != ""

def test_generate_comment():
    comment = Comment(
        id=fake.random_int(),
        body=fake.paragraph(),
        post_id=fake.random_int()
    )
    logging.info(f"Generated comment: {comment}")
    attach(comment.body, name="Comment Body", attachment_type=AttachmentType.TEXT)
    assert isinstance(comment.id, int)
    assert comment.body != ""
    assert isinstance(comment.post_id, int)

def test_generate_profile():
    profile = Profile(
        name=fake.name()
    )
    logging.info(f"Generated profile: {profile}")
    attach(profile.name, name="Profile Name", attachment_type=AttachmentType.TEXT)
    assert profile.name != ""

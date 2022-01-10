from flask import Blueprint, request
import logging

from api.logic.collections import CollectionsManager


api = Blueprint("collections_api", __name__)
log = logging.getLogger()

collectionsManager = CollectionsManager()


@api.route('/')
def index():
    log.warning("HELLO")
    log.info("WHY")

    log.warn("MESSAGE")
    log.error("ERROR")
    return "helloadda"

@api.route('/bard')
def bard():
    log.warn("YESS")
    log.info("YESAAADFDFA")
    return "aaaa"

@api.route('/documents')
def upload_document():
    pass

@api.route('/collections', methods=['POST'])
def create_collection():
    collectionsManager.create_collection('first_collection')
    return "a"

@api.route('/collections', methods=['GET'])
def get_collections():
    pass
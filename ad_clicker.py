from argparse import ArgumentParser
import requests
import re
import random
import time


from config import logger
from search_controller import SearchController



def get_arg_parser():
    
    arg_parser = ArgumentParser()
    arg_parser.add_argument("-q", "--query", help="Search query")
    arg_parser.add_argument("-t", "--visittime", default=4, type=int, dest="ad_visit_time",
                            help="Number of seconds to wait on the ad page opened")
    arg_parser.add_argument("-w", "--whitelist", default="", dest="white_list",
                            help="The website that you dont want to click on")
    return arg_parser


def main():

    arg_parser = get_arg_parser()
    args = arg_parser.parse_args()

    if not args.query:
        logger.error("Run with search query!")
        arg_parser.print_help()
        raise SystemExit()


    while True:
    #設定隨機間隔時間
        rest= random.randint(150,180)
        
        search_controller = SearchController(args.query,"127.0.0.1:9999", args.ad_visit_time)
        ads = search_controller.search_for_ads()

        if not ads:
            logger.info("No ads in the search results!")
            search_controller.end_search()
        else:
            logger.info(f"Found {len(ads)} ads")
            search_controller.click_ads(ads, args.white_list)
            search_controller.end_search()
            time.sleep(rest)
   


if __name__ == "__main__":

    main()

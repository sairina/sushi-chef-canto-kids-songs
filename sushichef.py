#!/usr/bin/env python

from le_utils.constants import licenses
from le_utils.constants.languages import getlang
from pressurecooker.youtube import YouTubeResource, is_youtube_subtitle_file_supported_language

from ricecooker.chefs import SushiChef
from ricecooker.classes.nodes import ChannelNode, TopicNode, VideoNode
from ricecooker.classes.files import YouTubeVideoFile, YouTubeSubtitleFile
# from ricecooker.classes.files import is_youtube_subtitle_file_supported_language
from ricecooker.classes.licenses import get_license

# import youtube_dl
# ydl = youtube_dl.YoutubeDL({
#     'quiet': True,
#     'no_warnings': True,
#     'writesubtitles': True,
#     'allsubtitles': True,
# })

class KidsSongsChef(SushiChef):
    channel_info = {
        "CHANNEL_TITLE": "Chinese Kids' Songs",
        "CHANNEL_SOURCE_DOMAIN": "youtube.com",  # where content comes from
        "CHANNEL_SOURCE_ID": "playlist",  # CHANGE ME!!!
        "CHANNEL_LANGUAGE": getlang('en').id,  # le_utils language code
        "CHANNEL_THUMBNAIL": 
            "./images/canto-thumbnail.jpg",  # (optional)
        "CHANNEL_DESCRIPTION": "Channel with Mandarin and Cantonese children's songs",  # (optional)
    }

    def construct_channel(self, **kwargs):
        channel = self.get_channel(**kwargs)
        canto_songs_topic = TopicNode(title="Cantonese Songs", source_id="canto-1")
        channel.add_child(canto_songs_topic)
        mandarin_songs_topic = TopicNode(title="Mandarin Songs", source_id="mandarin-1")
        channel.add_child(mandarin_songs_topic)

        # get all subtitles available for a sample video        
        # info = ydl.extract_info(youtube_id, download=False)
        # subtitle_languages = info["subtitles"].keys()
        # print('Found subtitle_languages = ', subtitle_languages)

        youtube_id='vBJB-C7pQ78'
        video_file1 = VideoNode(
            source_id=youtube_id,  # usually set source_id to youtube_id
            title='道理真巧妙',
            author='粵語兒歌',
            description='Song to the tune of Polly Wolly Doodle',
            language=getlang('en').id,
            license=get_license(licenses.PUBLIC_DOMAIN),
            derive_thumbnail=True,  # video-specicig flag
            thumbnail=None,
            files=[
                YouTubeVideoFile(youtube_id=youtube_id, high_resolution=False, language='zh-Hant')
                # YouTubeSubtitleFile(youtube_id=youtube_id, language='ko')
            ]
        )

        # add subtitles in whichever languages are available.
        # for lang_code in subtitle_languages:
        #     if is_youtube_subtitle_file_supported_language(lang_code):
        #         video_file1.add_file(
        #             YouTubeSubtitleFile(
        #                 youtube_id=youtube_id,
        #                 language=lang_code
        #             )
        #         )
        #         print(language)
        #     else:
                # print('Unsupported subtitle language code:', lang_code)

        youtube_id='Zo6nYCfygmc'
        video_file2 = VideoNode(
            source_id=youtube_id,  # usually set source_id to youtube_id
            title='小太陽',
            author='粵語兒歌',
            description='太陽像個大紅花　在那東方天邊掛  圓圓臉兒害羞像紅霞　只是笑不說話  太陽像個大南瓜　在那高高天空掛  照得滿山歡樂融融　草兒發嫩芽  大嘴巴　笑哈哈　落了也要往上爬  敬他　愛他　我把心願交給他  太陽倦了便回家　夜裡休息少驚怕  明晨月兒落旭日重來　依舊往上爬',
            language=getlang('en').id,
            license=get_license(licenses.PUBLIC_DOMAIN),
            derive_thumbnail=True,  # video-specicig flag
            thumbnail=None,
            files=[
                YouTubeVideoFile(youtube_id=youtube_id, high_resolution=False, language='en'),
            ]
        )
        
        youtube_id='Loc3MPVGhHU'
        video_file3 = VideoNode(
            source_id=youtube_id,  # usually set source_id to youtube_id
            title='兩隻老虎',
            author='經典兒歌',
            description='两只老虎 两只老虎 跑得快 跑得快 一只没有眼睛 一直没有耳朵 真奇怪 真奇怪',
            language=getlang('en').id,
            license=get_license(licenses.PUBLIC_DOMAIN),
            derive_thumbnail=True,  # video-specicig flag
            thumbnail=None,
            files=[
                YouTubeVideoFile(youtube_id=youtube_id, high_resolution=False, language='en'),
            ]
        )

        canto_songs_topic.add_child(video_file1)
        canto_songs_topic.add_child(video_file2)
        mandarin_songs_topic.add_child(video_file3)

        return channel


if __name__ == "__main__":
    """
    Run this script on the command line using:
        IF IN PROUCTION: python sushichef.py -v --reset --token=e430193a498433b36b79870f2feb0e1960ed03ec
        ELSE IF IN DEV: STUDIO_URL=http://localhost:8080 python sushichef.py --token=d935019dd1b179136bf8c2f338fe77fe13f357d3
    """
    simple_chef = KidsSongsChef()
    simple_chef.main()

    # chef = KidsSongsChef()
    # args = {
    #     'command': 'dryrun',  # use  'uploadchannel'  for real run
    #     'verbose': True,
    #     'token': 'd935019dd1b179136bf8c2f338fe77fe13f357d3'
    # }
    # options = {}
    # chef.run(args, options)
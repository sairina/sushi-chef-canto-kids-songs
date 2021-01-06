from ricecooker.chefs import SushiChef
from ricecooker.classes.nodes import ChannelNode, TopicNode, DocumentNode
from ricecooker.classes.files import DocumentFile
from ricecooker.classes.licenses import get_license


class ExploratoriumChef(SushiChef):
    channel_info = {
        "CHANNEL_TITLE": "Exploratorium",
        "CHANNEL_SOURCE_DOMAIN": "exploratorium.edu",  # where content comes from
        "CHANNEL_SOURCE_ID": "toolkit",  # CHANGE ME!!!
        "CHANNEL_LANGUAGE": "en",  # le_utils language code
        "CHANNEL_THUMBNAIL": 
            "sushicheffing/images/Exploratorium_logo_black_screen.png",  # (optional)
        "CHANNEL_DESCRIPTION": "Testing Exploratorium snacks",  # (optional)
    }

    def construct_channel(self, **kwargs):
        channel = self.get_channel(**kwargs)
        potato_topic = TopicNode(title="Potatoes!", source_id="<potatoes_id>")
        channel.add_child(potato_topic)
        document_node = DocumentNode(
            title="Growing potatoes",
            description="An article about growing potatoes on your rooftop.",
            source_id="pubs/mafri-potatoe",
            license=get_license("CC BY", copyright_holder="Exploratorium"),
            language="en",
            files=[
                DocumentFile(
                    path="https://www.gov.mb.ca/inr/pdf/pubs/mafri-potatoe.pdf",
                    language="en",
                )
            ],
        )
        potato_topic.add_child(document_node)
        return channel


if __name__ == "__main__":
    """
    Run this script on the command line using:
        IF IN PROUCTION: python sushichef.py -v --reset --token=e430193a498433b36b79870f2feb0e1960ed03ec
        ELSE IF IN DEV: STUDIO_URL=http://localhost:8080 python sushichef.py --token=d935019dd1b179136bf8c2f338fe77fe13f357d3
    """
    simple_chef = ExploratoriumChef()
    simple_chef.main()
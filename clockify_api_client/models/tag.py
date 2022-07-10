import logging
from urllib.parse import urlencode

from clockify_api_client.abstract_clockify import AbstractClockify


class Tag(AbstractClockify):

    def __init__(self, api_key, api_url):
        super(Tag, self).__init__(api_key=api_key, api_url=api_url)

    def get_tags(self, workspace_id, params=None):
        """Returns all tags.
        :param workspace_id Id of workspace to look for clients.
        :param params       URL params of request.
        :return             List of tags(dict objects).
        """
        try:
            if params:
                url_params = urlencode(params, doseq=True)
                url = self.base_url + '/workspaces/' + workspace_id + '/tags?' + url_params
            else:
                url = self.base_url + '/workspaces/' + workspace_id + '/tags/'
            return self.get(url)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    def add_tag(self, workspace_id, tag_name):
        """Add new client into workspace.
        :param workspace_id Id of workspace.
        :param tag_name name of tag
        :return             Dictionary representation of new tag.
        """
        try:
            url = self.base_url + '/workspaces/' + workspace_id + '/tags/'
            data = {
                'name': tag_name
            }
            return self.post(url, data)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

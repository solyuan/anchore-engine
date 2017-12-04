# coding: utf-8

"""
    anchore_engine.services.policy_engine

    This is a policy evaluation service. It receives push-events from external systems for data updates and provides an api for requesting image policy checks

    OpenAPI spec version: 1.0.0
    Contact: zach@anchore.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ImageUpdateNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'image_id': 'str',
        'user_id': 'str',
        'analysis_url': 'str',
        'event_timestamp': 'datetime'
    }

    attribute_map = {
        'image_id': 'image_id',
        'user_id': 'user_id',
        'analysis_url': 'analysis_url',
        'event_timestamp': 'event_timestamp'
    }

    def __init__(self, image_id=None, user_id=None, analysis_url=None, event_timestamp=None):
        """
        ImageUpdateNotification - a model defined in Swagger
        """

        self._image_id = None
        self._user_id = None
        self._analysis_url = None
        self._event_timestamp = None

        if image_id is not None:
          self.image_id = image_id
        if user_id is not None:
          self.user_id = user_id
        if analysis_url is not None:
          self.analysis_url = analysis_url
        if event_timestamp is not None:
          self.event_timestamp = event_timestamp

    @property
    def image_id(self):
        """
        Gets the image_id of this ImageUpdateNotification.

        :return: The image_id of this ImageUpdateNotification.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this ImageUpdateNotification.

        :param image_id: The image_id of this ImageUpdateNotification.
        :type: str
        """

        self._image_id = image_id

    @property
    def user_id(self):
        """
        Gets the user_id of this ImageUpdateNotification.

        :return: The user_id of this ImageUpdateNotification.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ImageUpdateNotification.

        :param user_id: The user_id of this ImageUpdateNotification.
        :type: str
        """

        self._user_id = user_id

    @property
    def analysis_url(self):
        """
        Gets the analysis_url of this ImageUpdateNotification.
        A url that can be used to retrieve the analysis information on the image

        :return: The analysis_url of this ImageUpdateNotification.
        :rtype: str
        """
        return self._analysis_url

    @analysis_url.setter
    def analysis_url(self, analysis_url):
        """
        Sets the analysis_url of this ImageUpdateNotification.
        A url that can be used to retrieve the analysis information on the image

        :param analysis_url: The analysis_url of this ImageUpdateNotification.
        :type: str
        """

        self._analysis_url = analysis_url

    @property
    def event_timestamp(self):
        """
        Gets the event_timestamp of this ImageUpdateNotification.
        The time of the external event. Should be set to when the event occurred, to the delivery time

        :return: The event_timestamp of this ImageUpdateNotification.
        :rtype: datetime
        """
        return self._event_timestamp

    @event_timestamp.setter
    def event_timestamp(self, event_timestamp):
        """
        Sets the event_timestamp of this ImageUpdateNotification.
        The time of the external event. Should be set to when the event occurred, to the delivery time

        :param event_timestamp: The event_timestamp of this ImageUpdateNotification.
        :type: datetime
        """

        self._event_timestamp = event_timestamp

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ImageUpdateNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

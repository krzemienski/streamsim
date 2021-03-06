__author__ = 'Alexander Dethof'

from bitstreamparse.rtpParser import RtpParser


class Mp2t(RtpParser):

    MP2TS_PAYLOAD_TYPE_ID = 33

    def _is_valid_payload_type(self, payload_type):
        assert isinstance(payload_type, int), 'Invalid payload type given!'

        return payload_type == self.MP2TS_PAYLOAD_TYPE_ID

    def _add_to_bit_stream(self, payload):
        self._bit_stream += payload
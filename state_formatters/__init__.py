from .dp_formatters import *
from .output_formatters import *

all_formatters = {
    'alice_formatter_dialog': alice_formatter_dialog,
    'eliza_formatter_dialog': eliza_formatter_dialog,
    'aiml_formatter_dialog': aiml_formatter_dialog,
    'cobot_qa_formatter_service': cobot_qa_formatter_service,
    'misheard_asr_formatter_service': misheard_asr_formatter_service,
    'base_skill_selector_formatter_dialog': base_skill_selector_formatter_dialog,
    'transfertransfo_formatter_dialog': transfertransfo_formatter_dialog,
    'personality_catcher_formatter_dialog': personality_catcher_formatter_dialog,
    'personality_catcher_formatter_service': personality_catcher_formatter_service,
    'cobot_classifiers_formatter_service': cobot_classifiers_formatter_service,
    'cobot_dialogact_formatter_service': cobot_dialogact_formatter_service,
    'cobot_formatter_dialog': cobot_formatter_dialog,
    'base_response_selector_formatter_service': base_response_selector_formatter_service,
    'sent_rewrite_formatter_dialog': sent_rewrite_formatter_dialog,
    'asr_formatter_dialog': asr_formatter_dialog,
    'last_utt_dialog': last_utt_dialog,
    'last_utt_and_history_dialog': last_utt_and_history_dialog,
    'dp_toxic_formatter_service': dp_toxic_formatter_service,
    'base_formatter_service': base_formatter_service,
    'simple_formatter_service': simple_formatter_service,
    'utt_sentseg_punct_dialog': utt_sentseg_punct_dialog,
    'utt_sentrewrite_modified_last_dialog': utt_sentrewrite_modified_last_dialog,
    'skill_with_attributes_formatter_service': skill_with_attributes_formatter_service,
    'last_utt_sentseg_punct_dialog': last_utt_sentseg_punct_dialog,
    'last_utt_sentseg_segments_dialog': last_utt_sentseg_segments_dialog,
    'attitude_formatter_service': attitude_formatter_service,
    'ner_formatter_dialog': ner_formatter_dialog,

    'http_debug_output_formatter': http_debug_output_formatter,
    'http_api_output_formatter': http_api_output_formatter,
}

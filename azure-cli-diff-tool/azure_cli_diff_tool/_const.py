# -----------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -----------------------------------------------------------------------------

import os
BLOB_SETTING_CONFIG_FILE = "./data/blob_config.ini"
script_directory = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE_PATH = f"{script_directory}/{BLOB_SETTING_CONFIG_FILE}"

META_CHANDE_WHITELIST_FILE = "./data/meta_change_whitelist.txt"
META_CHANDE_WHITELIST_FILE_PATH = f"{script_directory}/{META_CHANDE_WHITELIST_FILE}"
META_CHANDE_WHITELIST_FILE_URL = "https://azcmdchangemgmt.blob.core.windows.net/azure-cli-diff-tool-config/meta_change_whitelist.txt"
DOWNLOAD_THREADS = 30

BREAKING_CHANE_RULE_LINK_URL_PREFIX = "https://github.com/Azure/azure-cli/blob/dev/doc/breaking_change_rules/"
BREAKING_CHANE_RULE_LINK_URL_SUFFIX = ".md"

CMD_REMOVE_SUFFIX_WARN_LIST = ["wait"]

SUBGROUP_PROPERTY_REMOVE_BREAK_LIST = []
SUBGROUP_PROPERTY_REMOVE_WARN_LIST = ["deprecate_info_redirect"]

SUBGROUP_PROPERTY_ADD_BREAK_LIST = []
SUBGROUP_PROPERTY_ADD_WARN_LIST = ["deprecate_info_hide", "deprecate_info_expiration"]

SUBGROUP_PROPERTY_UPDATE_BREAK_LIST = []
SUBGROUP_PROPERTY_UPDATE_WARN_LIST = ["deprecate_info_expiration"]

SUBGROUP_PROPERTY_IGNORED_LIST = []

CMD_PROPERTY_REMOVE_BREAK_LIST = []
CMD_PROPERTY_REMOVE_WARN_LIST = ["deprecate_info_redirect"]

CMD_PROPERTY_ADD_BREAK_LIST = ["confirmation"]
CMD_PROPERTY_ADD_WARN_LIST = ["deprecate_info_hide", "deprecate_info_expiration"]

CMD_PROPERTY_UPDATE_BREAK_LIST = []
CMD_PROPERTY_UPDATE_WARN_LIST = ["deprecate_info_expiration", "deprecate_info_redirect"]

CMD_PROPERTY_IGNORED_LIST = ["is_aaz", "supports_no_wait"]

PARA_PROPERTY_REMOVE_BREAK_LIST = ["options"]
PARA_PROPERTY_REMOVE_WARN_LIST = ["id_part", "nargs", "deprecate_info_redirect"]

PARA_PROPERTY_ADD_BREAK_LIST = ["required"]
PARA_PROPERTY_ADD_WARN_LIST = ["choices", "deprecate_info_expiration", "deprecate_info_hide", "options_deprecate_info"]

PARA_PROPERTY_UPDATE_BREAK_LIST = ["default", "aaz_default"]
PARA_PROPERTY_UPDATE_WARN_LIST = ["type", "aaz_type", "choices", "nargs",
                                  "deprecate_info_expiration", "deprecate_info_redirect", "options_deprecate_info"]

PARA_NAME_IGNORED_LIST = ["force_string"]
PARA_PROPERTY_IGNORED_LIST = []
PARA_VALUE_IGNORED_LIST = ["generic_update_set", "generic_update_add", "generic_update_remove",
                           "generic_update_force_string"]

EXPORTED_CSV_META_HEADER = ["module", "cmd_name", "rule_id", "rule_name", "is_break", "diff_level",
                            "rule_link_url", "rule_message", "suggest_message"]

CHANGE_RULE_MESSAGE_MAPPING = {
    "1000": "default Message",
    "1001": "cmd `{0}` added",
    "1002": "cmd `{0}` removed",
    "1003": "cmd `{0}` added property `{1}`",
    "1004": "cmd `{0}` removed property `{1}`",
    "1005": "cmd `{0}` updated property `{1}` from `{2}` to `{3}`",
    "1006": "cmd `{0}` added parameter `{1}`",
    "1007": "cmd `{0}` removed parameter `{1}`",
    "1008": "cmd `{0}` update parameter `{1}`: added property `{2}={3}`",
    "1009": "cmd `{0}` update parameter `{1}`: removed property `{2}={3}`",
    "1010": "cmd `{0}` update parameter `{1}`: updated property `{2}` from `{3}` to `{4}`",
    "1011": "sub group `{0}` added",
    "1012": "sub group `{0}` removed",
    "1013": "sub group `{0}` added property `{1}`",
    "1014": "sub group `{0}` removed property `{1}`",
    "1015": "sub group `{0}` updated property `{1}` from `{2}` to `{3}`",
}

CHANGE_SUGGEST_MESSAGE_MAPPING = {
    "1000": "default Message",
    "1001": "please confirm cmd `{0}` added",
    "1002": "please confirm cmd `{0}` removed",
    "1003": "please remove property `{0}` for cmd `{1}`",
    "1004": "please add back property `{0}` for cmd `{1}`",
    "1005": "please change property `{0}` from `{1}` to `{2}` for cmd `{3}`",
    "1006": "please remove parameter `{0}` for cmd `{1}`",
    "1007": "please add back parameter `{0}` for cmd `{1}`",
    "1008": "please remove property `{0}={1}` for parameter `{2}` of cmd `{3}`",
    "1009": "please add back property `{0}={1}` for parameter `{2}` of cmd `{3}`",
    "1010": "please change property `{0}` from `{1}` to `{2}` for parameter `{3}` of cmd `{4}`",
    "1011": "please confirm sub group `{0}` added",
    "1012": "please confirm sub group `{0}` removed",
    "1013": "please remove property `{0}` for sub group `{1}`",
    "1014": "please add back property `{0}` for sub group `{1}`",
    "1015": "please change property `{0}` from `{1}` to `{2}` for sub group `{3}`",
}


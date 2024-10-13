from enum import Enum

class Type(str, Enum):
    photos = "photos"
    videos = "videos"

class Sort(str, Enum):
    asc = "asc"
    desc = "desc"

class Orientation(str, Enum):
    portrait = "portrait"
    landscape = "landscape"
    square = "square"

class Size(str, Enum):
    large = "large"
    medium = "medium"
    small = "small"

class Locale(str, Enum):
    en_US = "en-US"
    pt_BR = "pt-BR"
    es_ES = "es-ES"
    ca_ES = "ca-ES"
    de_DE = "de-DE"
    it_IT = "it-IT"
    fr_FR = "fr-FR"
    sv_SE = "sv-SE"
    id_ID = "id-ID"
    pl_PL = "pl-PL"
    ja_JP = "ja-JP"
    zh_TW = "zh-TW"
    zh_CN = "zh-CN"
    ko_KR = "ko-KR"
    th_TH = "th-TH"
    nl_NL = "nl-NL"
    hu_HU = "hu-HU"
    vi_VN = "vi-VN"
    cs_CZ = "cs-CZ"
    da_DK = "da-DK"
    fi_FI = "fi-FI"
    uk_UA = "uk-UA"
    el_GR = "el-GR"
    ro_RO = "ro-RO"
    nb_NO = "nb-NO"
    sk_SK = "sk-SK"
    tr_TR = "tr-TR"
    ru_RU = "ru-RU"


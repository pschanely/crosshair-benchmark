import re
from typing import Iterable, Optional, List, Set
from icontract import require, ensure

"""
This example is one simplified subset of the data generation tasks in:
https://github.com/aas-core-works/aas-crosshair

"""



class ValueList:
    value_reference_pairs: List[int]

    def __init__(self, value_reference_pairs: List[int]):
        self.value_reference_pairs = value_reference_pairs


class AbstractLangString:
    language: str
    text: str

    def __init__(self, language: str, text: str):
        self.language = language
        self.text = text


class LangStringPreferredNameTypeIEC61360(AbstractLangString):
    pass


class LangStringShortNameTypeIEC61360(AbstractLangString):
    pass


class LangStringDefinitionTypeIEC61360(AbstractLangString):
    pass


class DataSpecificationIEC61360:
    preferred_name: List["LangStringPreferredNameTypeIEC61360"]
    short_name: Optional[List["LangStringShortNameTypeIEC61360"]]
    unit: Optional[str]
    unit_id: Optional[int]
    source_of_definition: Optional[str]
    symbol: Optional[str]
    definition: Optional[List["LangStringDefinitionTypeIEC61360"]]
    value_format: Optional[str]
    value_list: Optional["ValueList"]
    value: Optional[str]

    def __init__(
        self,
        preferred_name: List["LangStringPreferredNameTypeIEC61360"],
        short_name: Optional[List["LangStringShortNameTypeIEC61360"]] = None,
        unit: Optional[str] = None,
        unit_id: Optional["int"] = None,
        source_of_definition: Optional[str] = None,
        symbol: Optional[str] = None,
        definition: Optional[List["LangStringDefinitionTypeIEC61360"]] = None,
        value_format: Optional[str] = None,
        value_list: Optional["ValueList"] = None,
        value: Optional[str] = None,
    ) -> None:
        self.preferred_name = preferred_name
        self.short_name = short_name
        self.unit = unit
        self.unit_id = unit_id
        self.source_of_definition = source_of_definition
        self.symbol = symbol
        self.definition = definition
        self.value_format = value_format
        self.value_list = value_list
        self.value = value


_REGEX_MATCHES_XML_SERIALIZABLE_STRING = re.compile(
    "^[\\x09\\x0a\\x0d\\x20-\\ud7ff\\ue000-\\ufffd\\U00010000-\\U0010ffff]*$"
)


def assert_value_list(that: ValueList) -> bool:
    assert len(that.value_reference_pairs) >= 1
    for p in that.value_reference_pairs:
        assert_non_empty_xml_serializable_string(p.value)


def assert_non_empty_xml_serializable_string(that: str) -> bool:
    assert _REGEX_MATCHES_XML_SERIALIZABLE_STRING.match(that) is not None
    assert len(that) >= 1


def lang_strings_have_unique_languages(
    lang_strings: Iterable[AbstractLangString],
) -> bool:
    language_set = set()  # type: Set[str]
    for lang_string in lang_strings:
        if lang_string.language in language_set:
            return False
        language_set.add(lang_string.language)
    return True


def is_data_specification_iec_61360(that: DataSpecificationIEC61360) -> bool:
    assert (((that.value is not None) and (that.value_list is None))) or (
        (
            (that.value is None)
            and (that.value_list is not None)
            and len(that.value_list.value_reference_pairs) >= 1
        )
    )
    assert not (that.short_name is not None) or (len(that.short_name) >= 1)
    assert not (that.short_name is not None) or lang_strings_have_unique_languages(
        that.short_name
    )
    assert len(that.preferred_name) >= 1
    assert lang_strings_have_unique_languages(that.preferred_name)
    if that.unit is not None:
        assert_non_empty_xml_serializable_string(that.unit)
    if that.source_of_definition is not None:
        assert_non_empty_xml_serializable_string(that.source_of_definition)
    if that.symbol is not None:
        assert_non_empty_xml_serializable_string(that.symbol)
    if that.value_format is not None:
        assert_non_empty_xml_serializable_string(that.value_format)
    if that.value_list is not None:
        assert_value_list(that.value_list)
    if that.value is not None:
        assert_non_empty_xml_serializable_string(that.value)
    return True


@require(lambda that: is_data_specification_iec_61360(that))
@ensure(lambda: False)
def play_with_data_specification_iec_61360(that: DataSpecificationIEC61360) -> None:
    pass

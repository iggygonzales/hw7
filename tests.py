import pytest
from textastic import Textastic
import textastic_parsers as tp

# Fixture to create an instance of Textastic for testing
@pytest.fixture
def textastic_instance():
    return Textastic()


# Test loading text using default parser
def test_load_text_default_parser(textastic_instance):
    textastic_instance.load_text('REPLACE FILE HERE', parser=tp.json_parser)


# Test loading text using custom parser
def test_load_text_custom_parser(textastic_instance):
    # Load text through parser
    textastic_instance.load_text('REPLACE FILE HERE', parser=Textastic._default_parser())


# Test loading stop words
def test_load_stop_words(textastic_instance):
    # Assuming stop words load properly
    textastic_instance.load_stop_words('stopwords.txt')


# Test word count visualization using Sankey diagram
def test_wordcount_sankey(textastic_instance):
    # Assuming Sankey diagram is generated properly
    textastic_instance.wordcount_sankey()


# Test comparing number of words using bar chart
def test_compare_num_words(textastic_instance):
    # Assuming the bar chart is generated properly
    textastic_instance.compare_num_words()


# Test word count visualization using subplot
def test_subplot(textastic_instance):
    # Assuming subplot is generated properly
    textastic_instance.subplot()


# Test word count visualization using overlay plot
def test_overlay(textastic_instance):
    # Assuming overlay plot is generated properly
    textastic_instance.overlay()

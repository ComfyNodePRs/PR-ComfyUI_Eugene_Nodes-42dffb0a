# Core Dictionary Management Nodes
class DictUpdate1:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "key": ("STRING", {"default": ""}),
                "value": ("STRING", {"multiline": True}),
            },
            "optional": {
                "input_dict": ("DICT",),
            }
        }

    RETURN_TYPES = ("DICT",)
    FUNCTION = "update_dict"
    CATEGORY = "dictionary/core"

    def update_dict(self, key, value, input_dict=None):
        result_dict = input_dict.copy() if input_dict else {}

        if key and value:
            result_dict[key] = value.strip()

        return (result_dict,)


class DictUpdate5:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "key1": ("STRING", {"default": ""}),
                "value1": ("STRING", {"multiline": True}),
            },
            "optional": {
                "input_dict": ("DICT",),
                "key2": ("STRING", {"default": ""}),
                "value2": ("STRING", {"multiline": True}),
                "key3": ("STRING", {"default": ""}),
                "value3": ("STRING", {"multiline": True}),
                "key4": ("STRING", {"default": ""}),
                "value4": ("STRING", {"multiline": True}),
                "key5": ("STRING", {"default": ""}),
                "value5": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES = ("DICT",)
    FUNCTION = "update_dict"
    CATEGORY = "dictionary/core"

    def update_dict(self, key1, value1, input_dict=None, key2="", value2="",
                   key3="", value3="", key4="", value4="", key5="", value5=""):
        result_dict = input_dict.copy() if input_dict else {}

        key_value_pairs = [
            (key1, value1), (key2, value2), (key3, value3),
            (key4, value4), (key5, value5)
        ]

        for key, value in key_value_pairs:
            if key and value:
                result_dict[key] = value.strip()

        return (result_dict,)


class DictUpdate10:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "key1": ("STRING", {"default": ""}),
                "value1": ("STRING", {"multiline": True}),
            },
            "optional": {
                "input_dict": ("DICT",),
                "key2": ("STRING", {"default": ""}),
                "value2": ("STRING", {"multiline": True}),
                "key3": ("STRING", {"default": ""}),
                "value3": ("STRING", {"multiline": True}),
                "key4": ("STRING", {"default": ""}),
                "value4": ("STRING", {"multiline": True}),
                "key5": ("STRING", {"default": ""}),
                "value5": ("STRING", {"multiline": True}),
                "key6": ("STRING", {"default": ""}),
                "value6": ("STRING", {"multiline": True}),
                "key7": ("STRING", {"default": ""}),
                "value7": ("STRING", {"multiline": True}),
                "key8": ("STRING", {"default": ""}),
                "value8": ("STRING", {"multiline": True}),
                "key9": ("STRING", {"default": ""}),
                "value9": ("STRING", {"multiline": True}),
                "key10": ("STRING", {"default": ""}),
                "value10": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES = ("DICT",)
    FUNCTION = "update_dict"
    CATEGORY = "dictionary/core"

    def update_dict(self, key1, value1, input_dict=None, key2="", value2="",
                   key3="", value3="", key4="", value4="", key5="", value5="",
                   key6="", value6="", key7="", value7="", key8="", value8="",
                   key9="", value9="", key10="", value10=""):
        result_dict = input_dict.copy() if input_dict else {}

        key_value_pairs = [
            (key1, value1), (key2, value2), (key3, value3),
            (key4, value4), (key5, value5), (key6, value6),
            (key7, value7), (key8, value8), (key9, value9),
            (key10, value10)
        ]

        for key, value in key_value_pairs:
            if key and value:
                result_dict[key] = value.strip()

        return (result_dict,)


# Dictionary Utility Nodes
class DictTemplate:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "template_text": ("STRING", {"multiline": True}),
                "dictionary": ("DICT", {})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "apply_template"
    CATEGORY = "dictionary/utils"

    def apply_template(self, template_text, dictionary):
        try:
            result = template_text
            for key, value in dictionary.items():
                placeholder = "{" + str(key) + "}"
                result = result.replace(placeholder, str(value))
            return (result,)
        except Exception as e:
            print(f"Error processing template: {str(e)}")
            return (template_text,)


class DictMultilineSelect:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_dict": ("DICT", {}),
                "line_number": ("INT", {"default": 0, "min": 0, "max": 9999}),
                "multiline_text": ("STRING", {"multiline": True}),
                "key_string": ("STRING", {})
            }
        }

    RETURN_TYPES = ("DICT", "INT")
    FUNCTION = "select_line"
    CATEGORY = "dictionary/utils"

    def select_line(self, input_dict, line_number, multiline_text, key_string):
        result_dict = dict(input_dict)
        lines = multiline_text.split('\n')

        if line_number >= len(lines):
            raise ValueError(f"Line number {line_number} is out of range. Text has {len(lines)} lines.")

        selected_line = lines[line_number].strip()
        result_dict[key_string] = selected_line

        return (result_dict, line_number)
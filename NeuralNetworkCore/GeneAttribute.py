class CGeneAttribute:
    def __init__(self, s_attribute_name, attribute_value):
        self._s_Attribute_Name = s_attribute_name
        self._attribute_Value = attribute_value

    def __eq__(self, other):
        b_return = False

        if(self._s_Attribute_Name == other._s_Attribute_Name and
           self._attribute_Value == other._attribute_Value):
            b_return = True

        return b_return

    def get_attribute_name(self):
        return self._s_Attribute_Name

    def get_attribute_value(self):
        return self._attribute_Value

    def set_attribute_value(self, attribute_value):
        self._attribute_Value = attribute_value

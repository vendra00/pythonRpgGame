from dataclasses import dataclass
from typing import Optional


@dataclass
class ImgPath:
    name: str
    partial_path: str
    parent_enum_name: Optional[str] = None

    def path(self, enums_dict):
        if self.parent_enum_name:
            parent_enum = enums_dict[self.parent_enum_name]
            parent_path = parent_enum.DEFAULT.path(enums_dict)  # Assuming each Enum has a DEFAULT key
            return f"{parent_path}{self.partial_path}"
        return self.partial_path



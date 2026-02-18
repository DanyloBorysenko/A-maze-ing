from pydantic import BaseModel, Field, model_validator, ValidationError
from typing import Dict, Tuple, Self, List
import sys


class Configuration(BaseModel):
    width: int = Field(ge=1, le=2147483648)
    height: int = Field(ge=1, le=2147483648)
    entry: Tuple[int, int]
    exit: Tuple[int, int]
    output_file: str = Field(min_length=5)
    perfect: bool

    @model_validator(mode="before")
    def create_tuples(cls, row_data: Dict) -> Dict:
        entry_x_y = row_data["entry"].split(",")
        exit_x_y = row_data["exit"].split(",")
        row_data["entry"] = tuple(entry_x_y)
        row_data["exit"] = tuple(exit_x_y)
        return row_data

    @model_validator(mode="after")
    def check_config(self) -> Self:
        if self.width == self.height:
            raise ValueError("Wrong size for maze")
        if self.entry == self.exit:
            raise ValueError("Entry must be different from exit")
        if self.entry[0] < 0 or self.entry[1] < 0:
            raise ValueError("Entry contains negative coordinates")
        if self.exit[0] < 0 or self.exit[1] < 0:
            raise ValueError("Exit contains negative coordinates")
        if self.entry[0] >= self.width:
            raise ValueError("Entry contains x coordinate bigger then width")
        if self.entry[1] >= self.height:
            raise ValueError("Entry contains y coordinate bigger then height")
        if self.exit[0] >= self.width:
            raise ValueError("Exit contains x coordinate bigger then width")
        if self.entry[1] >= self.height:
            raise ValueError("Exit contains y coordinate bigger then height")
        if not self.output_file.endswith(".txt"):
            raise ValueError("Output file name must contain '.txt'")
        return self


class ConfigParser():
    @staticmethod
    def parse_config(file_name: str) -> Configuration:
        row_data: Dict[str, str] = {}
        data: List[str]
        try:
            with open(file_name, mode="r") as f:
                data = f.readlines()
        except FileNotFoundError:
            print(f"File {file_name} not found", file=sys.stderr)
            exit(1)
        for line in data:
            if line.startswith("#") or line == "\n":
                continue
            line = line.strip("\n").strip().lower()
            key_value = line.split("=")
            row_data[key_value[0]] = key_value[1]
        try:
            return Configuration(**row_data)
        except ValidationError as e:
            print(e, sys.stderr)
            # print(e.errors()[0]["msg"], sys.stderr)
            exit(1)

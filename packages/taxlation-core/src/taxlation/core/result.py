from dataclasses import dataclass
from datetime import date,timedelta
import json

def _iso_duration(td: timedelta) -> str:
    sign = "-" if td < timedelta(0) else ""
    td = abs(td)
    hours, rem = divmod(td.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    sec = f"{seconds}.{td.microseconds:06d}".rstrip("0") if td.microseconds else str(seconds)
    date_part = f"{td.days}D" if td.days else ""
    time_part = "".join(f"{v}{u}" for v, u in ((hours, "H"), (minutes, "M"), (sec, "S")) if v not in (0, "0"))

    if not (date_part or time_part):
        return "PT0S"
    return f"{sign}P{date_part}" + (f"T{time_part}" if time_part else "")

def _serialize(v):
    if isinstance(v, date):        # dekt ook datetime (subklasse van date)
        return v.isoformat()
    if isinstance(v, timedelta):
        return _iso_duration(v)
    return v

@dataclass
class Result[T]:
    origin: str
    result: T
    explanation: str
    trail: tuple["Result", ...] = ()

    # def __bool__(self) -> bool:  # zodat je 'm nog in if/and kunt gebruiken
    #   if not isinstance(self.result, bool):
    #      raise TypeError(f"{self.result}: Result is not a bool.")
    #   return self.result

    def to_dict(self) -> dict:
      d = {
        "origin": self.origin,
        "result": _serialize(self.result),
        "explanation": self.explanation
      }

      if self.trail:
        d["trail"] = [s.to_dict() for s in self.trail]

      return d

    def __repr__(self) -> str:
       return json.dumps(self.to_dict(), ensure_ascii= False, indent=2)
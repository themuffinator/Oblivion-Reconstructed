import re
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
G_MISC_SOURCE = REPO_ROOT / "src" / "game" / "g_misc.c"
G_SPAWN_SOURCE = REPO_ROOT / "src" / "game" / "g_spawn.c"
BARRACKO_BSP = REPO_ROOT / "pack" / "maps" / "barracko.bsp"


def extract_function_block(source: str, function_name: str) -> str:
	pattern = re.compile(rf"{function_name}\s*\([^)]*\)\s*\{{", re.MULTILINE)
	match = pattern.search(source)
	if not match:
		raise AssertionError(f"Function {function_name} not found")
	start = match.end()
	depth = 1
	idx = start
	while idx < len(source) and depth > 0:
		char = source[idx]
		if char == "{":
			depth += 1
		elif char == "}":
			depth -= 1
		idx += 1
	return source[match.start():idx]


class InfoTeleporterDestRetailRegression(unittest.TestCase):
	@classmethod
	def setUpClass(cls) -> None:
		cls.g_misc_source = G_MISC_SOURCE.read_text(encoding="utf-8")
		cls.g_spawn_source = G_SPAWN_SOURCE.read_text(encoding="utf-8")
		cls.barracko_entities = BARRACKO_BSP.read_bytes().decode("latin-1", errors="ignore")

	def test_barracko_ships_a_typoed_info_teleporter_dest_pair(self) -> None:
		self.assertIn('"classname" "info_teleporter_dest"', self.barracko_entities)
		self.assertRegex(
			self.barracko_entities,
			re.compile(
				r'"classname" "info_teleporter_dest".*?"targetname" "tde".*?'
				r'"classname" "misc_teleporter".*?"target" "tde"',
				re.DOTALL,
			),
		)

	def test_ed_callspawn_keeps_unknown_classnames_in_place(self) -> None:
		callspawn_block = extract_function_block(self.g_spawn_source, "ED_CallSpawn")

		self.assertNotIn('{"info_teleporter_dest",', self.g_spawn_source)
		self.assertIn(
			'gi.dprintf ("%s doesn\'t have a spawn function\\n", ent->classname);',
			callspawn_block,
		)
		self.assertNotIn("G_FreeEdict (ent);", callspawn_block)
		self.assertNotIn("G_FreeEdict(ent);", callspawn_block)

	def test_stock_misc_teleporter_lookup_stays_targetname_only(self) -> None:
		teleporter_touch_block = extract_function_block(self.g_misc_source, "teleporter_touch")

		self.assertIn(
			"dest = G_Find (NULL, FOFS(targetname), self->target);",
			teleporter_touch_block,
		)
		self.assertNotIn("info_teleporter_dest", teleporter_touch_block)
		self.assertNotIn("info_teleport_dest", teleporter_touch_block)

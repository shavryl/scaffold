-- Running upgrade 01c18faa2821 -> e5bd3d3aec63

ALTER TABLE cookies RENAME TO new_cookies;

UPDATE alembic_version SET version_num='e5bd3d3aec63' WHERE alembic_version.version_num = '01c18faa2821';


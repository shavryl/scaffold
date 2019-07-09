"""Renaming cookies to new_cookies

Revision ID: e5bd3d3aec63
Revises: 01c18faa2821
Create Date: 2019-07-09 14:53:53.577040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5bd3d3aec63'
down_revision = '01c18faa2821'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('cookies', 'new_cookies')


def downgrade():
    op.rename_table('new_cookies', 'cookies')

"""add content column to post table

Revision ID: 5732cff9ebef
Revises: e2269b26f2ac
Create Date: 2022-08-14 06:54:31.722876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5732cff9ebef'
down_revision = 'e2269b26f2ac'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

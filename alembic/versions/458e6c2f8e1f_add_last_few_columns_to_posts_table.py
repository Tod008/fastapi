"""add last few columns to posts table

Revision ID: 458e6c2f8e1f
Revises: 6a3801db9904
Create Date: 2022-08-14 07:06:23.559363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '458e6c2f8e1f'
down_revision = '6a3801db9904'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass

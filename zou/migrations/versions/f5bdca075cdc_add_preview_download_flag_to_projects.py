"""add preview download flag to projects

Revision ID: f5bdca075cdc
Revises: f4ff5a73d283
Create Date: 2023-08-29 21:18:38.791600

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'f5bdca075cdc'
down_revision = 'f4ff5a73d283'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_preview_download_allowed', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_column('is_preview_download_allowed')

    # ### end Alembic commands ###

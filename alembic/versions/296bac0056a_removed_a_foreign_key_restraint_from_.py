"""Removed a foreign key restraint from the BanphraseData table.

Also added an enabled column to the Banphrase table

Revision ID: 296bac0056a
Revises: 1e79c9c63
Create Date: 2015-12-26 00:51:53.394838

"""

# revision identifiers, used by Alembic.
revision = '296bac0056a'
down_revision = '1e79c9c63'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_banphrase', sa.Column('enabled', sa.Boolean(), nullable=False))
    op.drop_constraint('tb_banphrase_data_ibfk_1', 'tb_banphrase_data', type_='foreignkey')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('tb_banphrase_data_ibfk_1', 'tb_banphrase_data', 'tb_user', ['added_by'], ['id'])
    op.drop_column('tb_banphrase', 'enabled')
    ### end Alembic commands ###

import discord
from discord.ext import commands

class lomba(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def input_data_lomba(self, ctx):
        pass

    @commands.command()
    async def hapus_data_lomba(self, ctx):
        pass

    @commands.command()
    async def daftar_lomba(self, ctx):
        await ctx.send("```Daftar Lomba\n1. Micin (UI/UX)\n2. Micin (Desain Produk)\n3. Micin (Competitive Programming)\nUntuk detail lengkap lomba silahkan tulis EDE!lomba_1(dummy trigger)```")

    @commands.command()
    async def detail_lomba(self, ctx):
        embed=discord.Embed(
            title="National Data Summit 2021", 
            url="https://docs.google.com/forms/d/e/1FAIpQLScUrTQt0Ne1OJ8Jw9JzBbLoS48YGa3K6Yq5JO8Z-tI_gdlo5g/viewform", 
            description="Dengan tema “Mewujudkan Indonesia Maju 2045 Melalui Penguasaan teknologi AI, Blockchain, dan Big Data”, NDS mengajak kamu untuk ikut serta dalam webinar dan kompetisi sebagai wadah bertukar pikiran dan mengasah skill dalam mengolah data.⁣⁣ ⁣⁣ Dengan tema kompetisi “Solusi Pembangunan Ekonomi Berkelanjutan Menuju Indonesia Maju 2045”.⁣⁣", 
            color=0x566acd)
        embed.add_field(name="Registrasi : ⁣", value="4 Oktober 2021 - 20 Oktober 2021", inline=False)
        embed.add_field(name="Batas Pengumpulan Berkas :", value="31 Oktober 2021", inline=False)
        embed.add_field(name="Pengumuman Finalis Terpilih :", value="8 November 2021⁣⁣", inline=False)
        embed.add_field(name="Kompetisi (final) :", value="20 November 2021⁣⁣", inline=False)
        embed.set_image(url="https://media.discordapp.net/attachments/897880106889007124/899676227122651184/unknown.png?width=494&height=671")
        embed.set_footer(text="Brought to you by HIMA MBTI x RC DBE⁣⁣ ⁣⁣")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(lomba(client))
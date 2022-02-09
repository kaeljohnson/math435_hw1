import org.apache.spark.api.java.function.PairFunction
import org.apache.spark.sql.SparkSession
import org.apache.spark.SparkContext

object NonidealPageRank {

  def main(args: Array[String]): Unit = {

    val sc = SparkSession.builder().master(args(0)).getOrCreate().sparkContext

    val lines = sc.textFile(args(1))

    val links = lines.map(s => (s.split(": ")(0), s.split(": ")(1)))


    val titles = sc.textFile(args(2)).zipWithIndex().mapValues(x=>(x+1).toString).map(_.swap)
    val numPages = titles.count()
    val zeroRankTitles = titles.mapValues(v => 0)
    var ranks = links.mapValues(v => 1.0/numPages)
    val jumpChance = 0.85
    val randomIncrement = (1 - jumpChance) / numPages


    for( i <- 1 to 25){
      var tempRank = links.join(ranks).values.flatMap{
        case(urls, rank) =>

          var outgoingLinks = urls.split(" ")
          outgoingLinks.map(url => (url, rank / outgoingLinks.size))

      }

    ranks = tempRank.reduceByKey(_ + _).fullOuterJoin(zeroRankTitles).mapValues{case(first, second) =>
      if(first == None){
        second.get
      }
      else{
        first.get
      }
    }.mapValues(x => jumpChance * x + randomIncrement)

    }
    val topTen = sc.parallelize(ranks.takeOrdered(10)(Ordering[Double].reverse.on(x=>x._2)))
    val fullNameTopTen = titles.join(topTen)
    fullNameTopTen.saveAsTextFile(args(3))


    println("Done..............")
  }
}
